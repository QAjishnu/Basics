import subprocess
import os
import re
import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class SVNDiffTool:
    def __init__(self, root):
        self.root = root
        self.root.title("SVN Tag Diff Automation Tool")
        self.root.geometry("600x520")
        self.root.resizable(False, False)

        self.root.columnconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        # --- 1. Repository Configuration Frame ---
        repo_frame = ttk.LabelFrame(self.root, text=" 1. SVN Repository Configuration ", padding=10)
        repo_frame.grid(row=0, column=0, padx=15, pady=15, sticky="ew")
        repo_frame.columnconfigure(1, weight=1)

        ttk.Label(repo_frame, text="Tags URL:").grid(row=0, column=0, sticky="w", pady=5)
        self.url_entry = ttk.Entry(repo_frame)
        self.url_entry.grid(row=0, column=1, columnspan=3, sticky="ew", pady=5, padx=(5, 0))
        self.url_entry.insert(0, "https://svn.ali.global/GDK_uslv/GDK_games/DragonVault_GLI/tags")

        ttk.Label(repo_frame, text="Username:").grid(row=1, column=0, sticky="w", pady=5)
        self.user_entry = ttk.Entry(repo_frame)
        self.user_entry.grid(row=1, column=1, sticky="ew", pady=5, padx=(5, 10))

        ttk.Label(repo_frame, text="Password:").grid(row=1, column=2, sticky="w", pady=5)
        self.pass_entry = ttk.Entry(repo_frame, show="*")
        self.pass_entry.grid(row=1, column=3, sticky="ew", pady=5, padx=(5, 0))

        # --- 2. Tag Selection Frame ---
        tag_frame = ttk.LabelFrame(self.root, text=" 2. Select Tags to Compare ", padding=10)
        tag_frame.grid(row=1, column=0, padx=15, pady=5, sticky="ew")
        tag_frame.columnconfigure(1, weight=1)

        self.fetch_btn = ttk.Button(tag_frame, text="Fetch Available Tags From SVN", command=self.fetch_tags)
        self.fetch_btn.grid(row=0, column=0, columnspan=2, pady=(5, 10), sticky="ew")

        ttk.Label(tag_frame, text="Base Tag (Older):").grid(row=1, column=0, sticky="w", pady=5)
        self.tag1_combo = ttk.Combobox(tag_frame, state="readonly")
        self.tag1_combo.grid(row=1, column=1, sticky="ew", pady=5, padx=(5, 0))

        ttk.Label(tag_frame, text="Target Tag (Newer):").grid(row=2, column=0, sticky="w", pady=5)
        self.tag2_combo = ttk.Combobox(tag_frame, state="readonly")
        self.tag2_combo.grid(row=2, column=1, sticky="ew", pady=5, padx=(5, 0))

        # --- 3. Execution Frame ---
        exec_frame = ttk.Frame(self.root, padding=10)
        exec_frame.grid(row=2, column=0, padx=15, pady=15, sticky="ew")
        exec_frame.columnconfigure(0, weight=1)

        self.diff_btn = ttk.Button(exec_frame, text="Generate Code Diff & Save File", command=self.generate_diff,
                                   state="disabled")
        self.diff_btn.grid(row=0, column=0, ipady=6, sticky="ew")

        # --- 4. Status Bar ---
        self.status_label = ttk.Label(self.root, text="Status: Ready", relief="sunken", anchor="w", padding=5)
        self.status_label.grid(row=3, column=0, sticky="ew", pady=(10, 0))

    def run_svn_command(self, args_list):
        """Arguments list use karke SVN run karne ka secure tariqa (No Shell Escape Issues)"""
        user = self.user_entry.get().strip()
        password = self.pass_entry.get().strip()

        if not user or not password:
            messagebox.showerror("Credentials Required", "Bhai, SVN Username aur Password dono daalna zaroori hai.")
            return None

        # Full command structure as an array/list
        full_command = (
                ['svn'] +
                args_list +
                ['--username', user, '--password', password, '--non-interactive', '--no-auth-cache']
        )

        try:
            # shell=False kiya hai taki credentials direct securely pass ho skein
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
            safe_error = e.stderr.replace(password, "********")
            messagebox.showerror("SVN Command Error", f"SVN running failed:\n\n{safe_error}")
            return None

    def fetch_tags(self):
        url = self.url_entry.get().strip()
        if not url or "example.com" in url:
            messagebox.showwarning("Invalid URL", "Pehle apna sahi SVN Tags URL daalo.")
            return

        self.update_status("Fetching tags from SVN server...")
        self.root.update_idletasks()

        # Passing arguments as list instead of text string
        output = self.run_svn_command(['list', url])

        if output:
            tags = [line.strip().rstrip('/') for line in output.splitlines() if line.strip()]
            tags.sort(key=lambda s: [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', s)], reverse=True)

            if len(tags) < 2:
                messagebox.showwarning("Insufficient Tags",
                                       f"Sirf yeh tags mile: {tags}\nDiff ke liye kam se kam 2 tags chahiye.")
                self.update_status("Ready")
                return

            self.tag1_combo['values'] = tags
            self.tag2_combo['values'] = tags

            self.tag1_combo.current(1)
            self.tag2_combo.current(0)

            self.diff_btn.config(state="normal")
            self.update_status(f"Success: {len(tags)} tags found.")
        else:
            self.update_status("Failed to extract tags.")

    def generate_diff(self):
        url = self.url_entry.get().strip()
        tag1 = self.tag1_combo.get()
        tag2 = self.tag2_combo.get()

        if tag1 == tag2:
            messagebox.showwarning("Selection Match", "Dono tags same nahi ho sakte. Alag tags select karo.")
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            initialfile=f"svn_diff_{tag1}_to_{tag2}.txt",
            title="Save Your Diff File"
        )

        if not save_path:
            return

        self.update_status("Running code diff analysis... Please wait...")
        self.root.update_idletasks()

        url1 = f"{url}/{tag1}"
        url2 = f"{url}/{tag2}"

        # Passing diff arguments safely as array elements
        diff_output = self.run_svn_command(['diff', url1, url2])

        if diff_output is not None:
            try:
                with open(save_path, "w", encoding="utf-8") as file:
                    file.write(f"=====================================\n")
                    file.write(f" SVN AUTOMATED CODE DIFF ANALYSIS\n")
                    file.write(f"=====================================\n")
                    file.write(f"Base Tag (Older):  {tag1}\n")
                    file.write(f"Target Tag (Newer): {tag2}\n")
                    file.write(f"=====================================\n\n")
                    file.write(diff_output)

                self.update_status("File saved successfully.")
                messagebox.showinfo("Success!", f"Bhai, file ready hai!\nYaha save hui hai:\n{save_path}")
            except Exception as e:
                messagebox.showerror("File Error", f"File write nahi ho payi:\n{str(e)}")
                self.update_status("Error saving file.")
        else:
            self.update_status("Diff generation failed.")

    def update_status(self, text):
        self.status_label.config(text=f"Status: {text}")


if __name__ == "__main__":
    window = tk.Tk()
    app = SVNDiffTool(window)
    window.mainloop()