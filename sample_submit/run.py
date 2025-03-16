import argparse
import pandas as pd
import pickle


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_data_path', type=str, help='test data path')
    parser.add_argument('--output_path', type=str, help='output file')
    args = parser.parse_args()

    test_data = pd.read_parquet(args.test_data_path)

    X_test = test_data['source_name'].str.lower()

    with open("baseline_vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
        
    X_test_tfidf = vectorizer.transform(X_test)

    with open("baseline_model.pkl", "rb") as f:
        model = pickle.load(f)

    # Предсказание
    y_pred = model.predict(X_test_tfidf)
    test_data['predicted_cat'] = y_pred
    test_data[['hash_id', 'predicted_cat']].to_csv(args.output_path, index=False)


if __name__ == "__main__":
    main()
