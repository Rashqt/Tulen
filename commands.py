# commands.py
import os
import shutil

def master_control_action(action, ctx):
    # placeholder dispatcher
    if action == "list":
        return {"status":"ok","msg":"Available actions: wipe_memory, shutdown, status"}
    return {"status":"error","msg":"unknown"}

def secure_wipe(folder_path):
    # WARNING: this is a best-effort demo. Real secure delete on SSDs is not guaranteed.
    # Better approach: encrypt all data and delete key.
    try:
        if os.path.exists(folder_path):
            # overwrite files (best-effort)
            for root, dirs, files in os.walk(folder_path):
                for fname in files:
                    fpath = os.path.join(root, fname)
                    try:
                        with open(fpath, "ba+") as f:
                            f.seek(0)
                            f.write(os.urandom(os.path.getsize(fpath) or 1))
                        os.remove(fpath)
                    except Exception:
                        pass
            shutil.rmtree(folder_path, ignore_errors=True)
            return True
    except Exception:
        pass
    return False
