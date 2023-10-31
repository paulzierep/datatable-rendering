from string import Template

import pandas as pd

df = pd.read_csv('microgalaxy_tools.csv', sep = "\t")
df["Expand"] = ""

df =  df.fillna('')

columns = ['Expand', 
           'Galaxy wrapper id', 
           'Galaxy wrapper version', 
           'Conda version', 
           'Conda id', 
           'Status', 
           'bio.tool id', 
           'bio.tool name', 
           'EDAM operation', 
           'EDAM topic',
           'Description',  
           'bio.tool description', 
           'Status', 
           'Source', 
           'ToolShed categories', 
           'ToolShed id', 
           'Galaxy wrapper owner', 
           'Galaxy wrapper source', 

           #'Reviewed', 
           #'To keep'
           ]

df = df.loc[:,columns]
df = df.reindex(columns=columns)

df.to_html('microgalaxy_tools.html', border = 0, table_id = "dataframe", classes = ["display","nowrap"], index=False)

final_html = []
with open('datatable_template.html', 'r') as template:
    final_html.append(template.read())

with open('microgalaxy_tools.html', 'r') as table:
    final_html.append(table.read())

final_html.append("</div>")

final_html_output = "\n".join(final_html)

with open("community_table.html", "w") as output:
    output.write(final_html_output) 