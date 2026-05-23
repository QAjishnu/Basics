import streamlit as st
import subprocess
import re

# Page layout setup
st.set_page_config(page_title="SVN Bulk Side-by-Side Diff", page_icon="📝", layout="centered")

st.title("📝 SVN Bulk Side-by-Side Report Generator")
st.markdown(
    "Yeh tool badli hui files ke naam aur unka side-by-side diff ek single organized text file mein generate karta hai.")

if 'tags_list' not in st.session_state:
    st.session_state.tags_list = []


def run_svn_command(args_list, user, password):
    full_command = (
            ['svn'] +
            args_list +
            ['--username', user, '--password', password, '--non-interactive', '--no-auth-cache']
    )
    try:
        result = subprocess.run(
            full_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=False,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        if e.stdout:
            return e.stdout
        return None


# --- UI Section 1: SVN Configuration ---
st.header("1. SVN Repository Configuration")
url = st.text_input("Tags URL:", "https://svn.ali.global/GDK_uslv/GDK_games/DragonVault_GLI/tags")

col1, col2 = st.columns(2)
with col1:
    user = st.text_input("Username:")
with col2:
    password = st.text_input("Password:", type="password")

if st.button("Fetch Available Tags From SVN", type="primary"):
    with st.spinner("Tags fetch ho rahe hain..."):
        output = run_svn_command(['list', url], user, password)
        if output:
            tags = [line.strip().rstrip('/') for line in output.splitlines() if line.strip()]
            tags.sort(key=lambda s: [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', s)], reverse=True)
            if len(tags) < 2:
                st.warning(f"Kam se kam 2 tags chahiye.")
            else:
                st.session_state.tags_list = tags
                st.success("Tags mil gaye!")

# --- UI Section 2: Bulk Selection & File Processing ---
if st.session_state.tags_list:
    st.header("2. Select Tags to Compare")
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        tag1 = st.selectbox("Base Tag (Older / Left Side):", st.session_state.tags_list, index=1)
    with col_t2:
        tag2 = st.selectbox("Target Tag (Newer / Right Side):", st.session_state.tags_list, index=0)

    if tag1 != tag2:
        if st.button("🚀 Generate Full Side-by-Side File"):
            with st.spinner("Analyzing changes and scanning files..."):
                url1 = f"{url}/{tag1}"
                url2 = f"{url}/{tag2}"

                # Step 1: Pehle badli hui files ki list fetch karo
                summary_output = run_svn_command(['diff', '--summarize', url1, url2], user, password)

                if summary_output:
                    changed_files = []
                    for line in summary_output.splitlines():
                        parts = line.split(None, 1)
                        if len(parts) == 2:
                            status, file_url = parts
                            file_url = file_url.strip()

                            # Skip folders
                            if file_url.endswith('/') or file_url == url1 or file_url == url2:
                                continue

                            if status in ['M', 'A']:
                                display_name = file_url.split(f"/{tag2}/")[-1]
                                changed_files.append(
                                    {"status": status, "full_url": file_url, "display_name": display_name})

                    total_files = len(changed_files)

                    if total_files == 0:
                        st.info("Dono tags ke beech koi valid file changes nahi mile.")
                    else:
                        st.write(
                            f"Total **{total_files}** files mili hain. Sabka side-by-side diff compile ho raha hai...")

                        # Progress reporting UI placeholders
                        status_text = st.empty()
                        progress_bar = st.progress(0)

                        # --- REPORT WRITING: Build Header and File Summary List ---
                        report_lines = []
                        report_lines.append(
                            "==========================================================================")
                        report_lines.append(
                            "               SVN BULK FILE-WISE SIDE-BY-SIDE DIFF REPORT                ")
                        report_lines.append(
                            "==========================================================================")
                        report_lines.append(f" Older Tag (Left Side):  {tag1}")
                        report_lines.append(f" Newer Tag (Right Side): {tag2}")
                        report_lines.append(f" Total Changed Files:    {total_files}")
                        report_lines.append(" Symbols Note: '|' = Modified, '<' = Deleted line, '>' = Added line")
                        report_lines.append(
                            "==========================================================================\n")

                        report_lines.append("📋 LIST OF CHANGED FILES IN THIS REPORT:")
                        report_lines.append("-----------------------------------------")
                        for idx, f in enumerate(changed_files, 1):
                            report_lines.append(f" {idx}. [{f['status']}] {f['display_name']}")
                        report_lines.append(
                            "\n==========================================================================\n\n")

                        # Step 2: Loop automatically through each file and fetch code diff
                        for index, f in enumerate(changed_files):
                            f_url_tag2 = f['full_url']
                            f_url_tag1 = f_url_tag2.replace(f"/{tag2}", f"/{tag1}")

                            current_index = index + 1
                            percentage = int((current_index / total_files) * 100)
                            status_text.markdown(
                                f"⏳ Processing file **{current_index}** of **{total_files}** — **{percentage}%**")
                            progress_bar.progress(current_index / total_files)

                            # Native SVN Side-by-Side configuration for individual files
                            single_diff_args = ['diff', '--extensions', '-y --width 150', f_url_tag1, f_url_tag2]
                            file_diff_output = run_svn_command(single_diff_args, user, password)

                            # Append dynamic file headers and content inside report body
                            report_lines.append(
                                f"👉 FILE {current_index}/{total_files}: [{f['status']}] {f['display_name']}")
                            report_lines.append("-" * 130)
                            if file_diff_output and file_diff_output.strip():
                                report_lines.append(file_diff_output)
                            else:
                                report_lines.append("[No text differences found or binary file content skipped]\n")
                            report_lines.append("\n" + "=" * 130 + "\n\n")

                        # Clear UI indicators once loop finishes
                        status_text.empty()
                        progress_bar.empty()

                        # Combine all lines into the final text format string
                        final_text_report = "\n".join(report_lines)
                        st.success("Poori report files ke naam aur side-by-side diff ke sath ready hai!")

                        # Step 3: Server Download button for final comprehensive file
                        st.download_button(
                            label="📥 Download Full Side-by-Side Text Report",
                            data=final_text_report,
                            file_name=f"svn_bulk_side_by_side_{tag1}_to_{tag2}.txt",
                            mime="text/plain"
                        )
                else:

                    st.error("Summary scan failed. Ek baar VPN aur credentials check karein bhai.")