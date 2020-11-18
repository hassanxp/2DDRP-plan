import plotly.figure_factory as ff
import plotly.graph_objs as go


def addAnnotation(df, fig):

    c = 0
    for i in df:
        # fig['layout']['annotations'] += tuple([dict(x=i.get("Finish"),y=c,text=f"{i.get('Task')}", showarrow=True, font=dict(color='black'))])
        fig['layout']['annotations'] += tuple([dict(x=i.get("Finish"), y=c, xanchor='right', yanchor='middle', text=f"{i.get('Task')}", showarrow=True, font=dict(color='black'))])
        c = c + 1

StartA = '2009-01-01'
StartB = '2009-03-05'
StartC = '2009-02-20'

FinishA='2009-02-28'
FinishB='2009-04-15'
FinishC='2009-05-30'

df = [dict(Task="Task A", Start=StartA, Finish=FinishA),
      dict(Task="Task B", Start=StartB, Finish=FinishB),
      dict(Task="Task C", Start=StartC, Finish=FinishC)]

fig = ff.create_gantt(df)


addAnnotation(df, fig)

fig.show(renderer='chrome')
