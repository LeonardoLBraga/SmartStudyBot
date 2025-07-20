"""
main.py

Main entry point for SmartStudyBot application.
Handles initializing and running the main program loop.
"""

import logging
import sys
from rich.logging import RichHandler
from modules import summarize, tts, resource_fetcher, question_recommender, usage_guide

logging.basicConfig(
    level=logging.INFO, format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
)
logger = logging.getLogger("rich")


def main():
    """
    Main function to start the SmartStudyBot application.
    """

    logging.info("🤖 Welcome to SmartStudyBot!")
    logging.info("1. Summarize a topic")
    logging.info("2. Get study resources")
    logging.info("3. Practice questions")
    logging.info("4. Hear a response")
    logging.info("5. Help!")
    logging.info("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        topic = input("Enter topic: ")
        summary = summarize.generate_summary(topic)
        logging.info("\n🔎 Summary:\n%s", summary)

    elif choice == "2":
        topic = input("Enter topic: ")
        links = resource_fetcher.fetch_resources(topic)
        logging.info("\n📚 Study Resources:")
        for link in links:
            logging.info("%s", link)

    elif choice == "3":
        subject = input("Enter subject (python/dsa): ").lower()
        question_recommender.ask_questions(subject)

    elif choice == "4":
        text = input("Enter what you want to hear: ")
        tts.speak(text)

    elif choice == "5":
        usage_guide.show_help()

    elif choice == "6":
        logging.info("👋 Goodbye!")
        sys.exit()

    else:
        logging.error("❌ Invalid choice. Exiting.")


if __name__ == "__main__":
    main()
