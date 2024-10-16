import pandas as pd

def handle_uploaded_file(file):
    """
    This function processes the uploaded Excel/CSV file and generates a summary.
    """
    # Read the file based on the extension
    if file.name.endswith('.xlsx'):
        data = pd.read_excel(file)
    elif file.name.endswith('.csv'):
        data = pd.read_csv(file)
    else:
        raise ValueError("Unsupported file type")

    # Generate a summary report based on the file content
    summary = []
    summary.append(f"File Name: {file.name}")
    summary.append(f"Number of Rows: {len(data)}")
    summary.append(f"Number of Columns: {len(data.columns)}")
    summary.append(f"Column Names: {', '.join(data.columns)}")
    
    # Add basic statistics if the data has numerical columns
    numerical_summary = data.describe().to_string()
    summary.append("\nBasic Statistics:\n")
    summary.append(numerical_summary)

    return "\n".join(summary)
