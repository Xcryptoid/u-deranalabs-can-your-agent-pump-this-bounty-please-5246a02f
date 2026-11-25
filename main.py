import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    # The hype line lives in entry.txt already written; this step
    # only carries that finished line into the graded output folder.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.txt"),
        os.path.join(out_dir, "entry.txt"),
    )


if __name__ == "__main__":
    main()
