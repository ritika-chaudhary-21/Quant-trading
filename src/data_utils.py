def load_and_concat_csv(folder_path):
    files = glob.glob(os.path.join(folder_path, "*.csv"))
    print(f"Found {len(files)} files in {folder_path}")

    df_list = []
    for file in files:
        df = pd.read_csv(file, low_memory=False)
        df_list.append(df)

    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df

def clean_columns(df):
    df.columns = (
        df.columns
          .str.strip()
          .str.replace(r"\s+", " ", regex=True)
    )
    return df

