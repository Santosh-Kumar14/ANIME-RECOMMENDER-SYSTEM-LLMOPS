from src.data_loader import anime_data_loader
from src.vector_store import vector_store_builder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger=get_logger(__name__)

def main():
    try:
        logger.info("Starting the build pipeline....")
        loader=anime_data_loader("data/anime_with_synopsis.csv","data/anime_with_synopsis_processed.csv")
        processed_csv=loader.load_and_process()

        logger.info("Data Loaded and Processed....")

        vector_builder=vector_store_builder(processed_csv)
        vector_builder.build_and_save_vectorstore()

        logger.info("Vector Store Built Successfully...")

        logger.info("Pipeline Built Successfully...." )


    except Exception as e:
            logger.error(f"Failed to execute pipeline {str(e)}")
            raise CustomException("Error during pipeline execution",e)

if __name__=="__main__":
     main()