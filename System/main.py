"""
MAIN – Final Batch Processing Pipeline
Progetto Tesi – Event Classification Workflow
"""

from workflow.database.init_db import init_db
from workflow.database.clear_db import clear_db
from workflow.pipelines.ufficial_pipeline import FinalBatchPipeline


CSV_PATH = "workflow/data/event_static_100_tests.csv"
CLEAR_DB_BEFORE_RUN = True

def main():
    print("\n====================")
    print("   EVENT WORKFLOW")
    print("====================\n")

    # ---------------------------------------
    # 1) INIT DB
    # ---------------------------------------
    print("[1] Initializing database...")
    init_db()

    # ---------------------------------------
    # 2) CLEAR DB (optional)
    # ---------------------------------------
       
    if CLEAR_DB_BEFORE_RUN:
        print("[2] Clearing previous DB content...")
        clear_db()

    # ---------------------------------------
    # 3) BUILD FINAL PIPELINE
    # ---------------------------------------
    print("[3] Building final batch pipeline...")
    pipeline = FinalBatchPipeline(csv_path=CSV_PATH)

    # ---------------------------------------
    # 4) EXECUTE
    # ---------------------------------------
    print("[4] Running processing of 100 events...\n")
    pipeline.run(limit=100)

    print("\n====================")
    print("   WORKFLOW COMPLETED")
    print("====================\n")


if __name__ == "__main__":
    main()
