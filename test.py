import pandas as pd
from utils import download_images
from model import process_image


def main():
    # Load train and test datasets
    test_df = pd.read_csv('dataset/test.csv')

    # Download images for the test set
    test_images = test_df['image_link'].tolist()
    download_images(test_images, 'images/test')

    # Prepare predictions for the test set
    predictions = []
    for index, row in test_df.iterrows():
        image_path = f"images/test/image_{index}.jpg"
        entity_name = row['entity_name']

        prediction = process_image(image_path, entity_name)
        if not prediction:
            prediction = ""  # Return an empty string if no valid prediction

        predictions.append([row['index'], prediction])

    # Create the output dataframe
    output_df = pd.DataFrame(predictions, columns=['index', 'prediction'])

    # Save the predictions to a CSV file
    output_df.to_csv('test_out.csv', index=False)
    print("Predictions saved to test_out.csv")


if __name__ == "__main__":
    main()
