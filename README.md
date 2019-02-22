# class05
Class 05: Van Quang Nguyen

1. Import libraries.
2. Use argparse to detect filename.
3. If file exists, do the following:

	3.1 Read data as df.
	3.2 Display some first rows of df.
	3.3 Display the statistical summary of df.
	3.4 One-feature visualization:
		3.4.1. Extract columns' names as cols.
		3.4.2. For columns in cols:
			3.4.2.1. Plot histogram.
			3.4.2.2. Save the plot.
	3.5. Two-features visualization:
		3.5.1. Initialize the list of all colums as all_cols.
		3.5.2. For col1 in cols do the following:
			3.5.2.1. Eliminate col1 from all_cols.
			3.5.2.2. For col2 in all_cols do:
				3.5.2.2.1. Scatter plot of col1 and col2.
				3.5.2.2.2. Save figure.
	3.6. Add header:
		3.6.1. Create a series consisting of names of columns.
		3.6.2. Add this series to df.
	3.7. Many-features visualization:
		3.7.1. Determine all the necessary features.
		3.7.2. Create new data frame of these features.
		3.7.3. Plot heatmap of the created data frame.
		3.7.4. Save the figure.
		3.7.5. Show the figure.

