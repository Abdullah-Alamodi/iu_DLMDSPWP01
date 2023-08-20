import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure, show
from numpy import array, histogram


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
            p.circle(x=df[x_axis], 
                     y=df[y_axis], 
                     size=10)
            p.xaxis.axis_label=x_axis
            p.yaxis.axis_label=y_axis
            show(p)
        else:
            plt.figure()
            plt.plot(df[x_axis], df[y_axis], label=y_axis)
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.legend()
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
            p.vbar(x=df[x_axis], top=df[y_axis], line_color='white')
            p.xaxis.axis_label=x_axis
            p.yaxis.axis_label=y_axis
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
        from scipy.stats import linregress

        df = self.df
        slope, intercept, r_value, p_value, std_err = linregress(df[x_axis], df[y_axis])

        if interactive:
            p = figure(title=title)
            p.circle(x=df[x_axis], y=df[y_axis])
            p.xaxis.axis_label=x_axis
            p.yaxis.axis_label=y_axis
            x_range = array([min(df[x_axis]), max(df[x_axis])])
            y_range = intercept + slope * x_range
            p.line(x=x_range, y=y_range, line_width=2, color='red')
            show(p)
        else:
            sns.scatterplot(x=x_axis, y=y_axis, data=df)
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            x_range = array([min(df[x_axis]), max(df[x_axis])])
            y_range = intercept + slope * x_range
            plt.plot(x_range, y_range, color='red', linewidth=2)
            plt.show()

        # df = self.df
        # if interactive:
        #     p = figure(title=title)
        #     p.circle(x=df[x_axis], y=df[y_axis])
        #     p.xaxis.axis_label=x_axis
        #     p.yaxis.axis_label=y_axis
        #     p.yaxis.axis_label = y_axis
        #     p.line(
        #         x=[min(df[x_axis]), max(df[x_axis])],
        #         y=[min(df[y_axis]), max(df[y_axis])],
        #         line_width=2,
        #         color="red")
        #     show(p)
        # else:
        #     sns.scatterplot(x=x_axis, y=y_axis, data=df)
        #     plt.title(title)
        #     plt.xlabel(x_label)
        #     plt.ylabel(y_label)
        #     plt.plot([min(df[x_axis]), max(df[x_axis])], [min(df[y_axis]), max(df[y_axis])], color='red', linewidth=2)
        #     plt.show()

    def histogram(self, 
                  x_axis, 
                  title, 
                  x_label=None, 
                  interactive=False):
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
            p = figure(title=title, x_axis_label=x_axis)
            hist, edges = histogram(df[x_axis], density=True, bins=50)
            p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="navy", line_color="white", alpha=0.5)
            show(p)
        else:
            sns.histplot(df[x_axis])
            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel("Number of passengers")
            plt.show()