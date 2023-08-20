import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure, show


class Visualization:
    def __init__(self, df):
        self.df = df

    def line_plot(self, 
                  x_axis, 
                  y_axis, 
                  title=None, 
                  x_label=None, 
                  y_label=None, 
                  interactive=False):
        """
        Creates a line plot of the given data.

        Parameters
        ----------
        x_axis: str
            Column name of the x-axis.
        y_axis: str
            Column name of the y-axis.
        title: str 
            Title of the plot.
        x_label: str
            Label for the x-axis.
        y_label: str 
            Label for the y-axis.
        interactive: bool
            Boolean flag to indicate whether to create an interactive graph.
        """
        df = self.df
        if interactive:
            p = figure(title=title)
            p.circle(x=df[x_axis], y=df[y_axis], size=10)
            show(p)
        else:
            plt.figure()
            plt.plot(df[x_axis], df[y_axis])
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.show()

    def bar_chart(self, 
                  x_axis, 
                  y_axis, 
                  title=None, 
                  x_label=None, 
                  y_label=None, 
                  interactive=False):
        """
        Creates a bar chart of the given data.

        Parameters
        ----------
        x_axis: str
            Column name of the x-axis.
        y_axis: str
            Column name of the y-axis.
        title: str
            Title of the plot.
        x_label: str
            Label for the x-axis.
        y_label: str
            Label for the y-axis.
        interactive: bool
            Boolean flag to indicate whether to create an interactive graph.
        """
        df = self.df
        if interactive:
            p = figure(title=title)
            p.vbar(x=df[x_axis], top=df[y_axis])
            show(p)
        else:
            sns.barplot(x=x_axis, y=y_axis, data=df)
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.show()

    def scatter_plot(self, 
                     x_axis, 
                     y_axis, 
                     title, 
                     x_label=None, 
                     y_label=None, 
                     interactive=False):
        """
        Creates a scatter plot of the given data.

        Parameters
        ----------
        x_axis: str
            Column name of the x-axis.
        y_axis: str
            Column name of the y-axis.
        title: str
            Title of the plot.
        x_label: str
            Label for the x-axis.
        y_label: str
            Label for the y-axis.
        interactive: bool
            Boolean flag to indicate whether to create an interactive graph.
        """
        df = self.df
        if interactive:
            sns.scatterplot(x=x_axis, y=y_axis, data=df)
            show()
        else:
            sns.scatterplot(x=x_axis, y=y_axis, data=df)
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.show()

    def histogram(self, x_axis, title, x_label, interactive=False):
        """
        Creates a histogram of the given data.

        Parameters
        ----------
        x_axis: str
            Column name of the x-axis.
        title: str
            Title of the plot.
        x_label: str
            Label for the x-axis.
        interactive: bool
            Boolean flag to indicate whether to create an interactive graph.
        """
        df = self.df
        if interactive:
            sns.histplot(df[x_axis])
            show()
        else:
            sns.histplot(df[x_axis])
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel("Number of passengers")
            plt.show()

from sql import SQL
sql = SQL(db_name="iudatabase")
df = sql.read_table(table_name="train")
vis = Visualization(df=df)
print(vis.bar_chart("x", "y1", "Test", interactive=True))

#====================================
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from bokeh.plotting import figure, show

# class Graph:
#     def __init__(self, file_path):
#         """
#         Initializes the Graph object and reads the data from the given file path.
        
#         :param file_path: The path to the file containing the data.
#         :type file_path: str
#         """
#         self.data = pd.read_csv(file_path)

#     def line_plot(self, x, y, title=None, interactive=False):
#         """
#         Creates a line plot using the given x and y data.
        
#         :param x: The x data for the plot.
#         :type x: list
#         :param y: The y data for the plot.
#         :type y: list
#         :param title: The title of the plot, defaults to None
#         :type title: str, optional
#         :param interactive: Whether to create an interactive plot, defaults to False
#         :type interactive: bool, optional
#         """
#         if interactive:
#             p = figure(title=title)
#             p.line(x, y)
#             show(p)
#         else:
#             plt.plot(x, y)
#             if title:
#                 plt.title(title)
#             plt.show()

#     def bar_chart(self, x, y, title=None, interactive=False):
#         """
#         Creates a bar chart using the given x and y data.
        
#         :param x: The x data for the chart.
#         :type x: list
#         :param y: The y data for the chart.
#         :type y: list
#         :param title: The title of the chart, defaults to None
#         :type title: str, optional
#         :param interactive: Whether to create an interactive chart, defaults to False
#         :type interactive: bool, optional
#         """
#         if interactive:
#             p = figure(title=title)
#             p.vbar(x=x, top=y)
#             show(p)
#         else:
#             plt.bar(x, y)
#             if title:
#                 plt.title(title)
#             plt.show()

#     def scatter_plot(self, x, y, title=None, interactive=False):
#         """
#         Creates a scatter plot using the given x and y data.
        
#         :param x: The x data for the plot.
#         :type x: list
#         :param y: The y data for the plot.
#         :type y: list
#         :param title: The title of the plot, defaults to None
#         :type title: str, optional
#         :param interactive: Whether to create an interactive plot, defaults to False
#         :type interactive: bool, optional
#         """
#         if interactive:
#             p = figure(title=title)
#             p.circle(x=x, y=y)
#             show(p)
#         else:
#             plt.scatter(x, y)
#             if title:
#                 plt.title(title)
#             plt.show()

#     def histogram(self, data, bins=None, title=None, interactive=False):
#         """
#         Creates a histogram using the given data.
        
#         :param data: The data for the histogram.
#         :type data: list
#         :param bins: The number of bins for the histogram, defaults to None
#         :type bins: int, optional
#         :param title: The title of the histogram, defaults to None
#         :type title: str, optional
#          :param interactive: Whether to create an interactive histogram, defaults to False
#          :type interactive: bool, optional
#          """
#         if bins:
#              if interactive:
#                  p = figure(title=title)
#                  hist_data = np.histogram(data,bins=bins)[0]
#                  p.quad(top=hist_data,bottom=0,left=bins[:-1],right=bins[1:])
#                  show(p)
#              else:
#                  plt.hist(data,bins=bins)
#                  if title:
#                      plt.title(title)
#                  plt.show()
