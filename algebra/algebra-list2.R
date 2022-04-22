library(ggplot2)
library(dplyr)

# Create data (this takes more sense with a numerical X axis)
x <- seq(1, 20)
data <- data.frame(
  x=x, 
  y=runif(20, -25.0, 45.0)
)

# Add a column with your condition for the color
data <- data %>% 
  mutate(mycolor = ifelse(y>0, 'color1', 'color2'))

# plot
ggplot(data, aes(x=x, y=y)) +
  geom_segment( aes(x=x, xend=x, y=0, yend=y, color=mycolor), size=1.3, alpha=0.9) +
  theme_light() +
  theme(
    legend.position = "none",
    panel.border = element_blank(),
  ) +
  xlab("Day") +
  ylab("Temperature")

# Libraries
library(igraph)
library(networkD3)

# create a dataset:
data <- data_frame(
  from=c("A", "A", "B", "D", "C", "D", "E", "B", "C", "D", "K", "A", "M"),
  to=c("B", "E", "F", "A", "C", "A", "B", "Z", "A", "C", "A", "B", "K")
)

# Plot
p <- simpleNetwork(data, height="100px", width="100px",        
                   Source = 1,                 # column number of source
                   Target = 2,                 # column number of target
                   linkDistance = 10,          # distance between node. Increase this value to have more space between nodes
                   charge = -900,                # numeric value indicating either the strength of the node repulsion (negative value) or attraction (positive value)
                   fontSize = 14,               # size of the node names
                   fontFamily = "serif",       # font og node names
                   linkColour = "#666",        # colour of edges, MUST be a common colour for the whole graph
                   nodeColour = "#69b3a2",     # colour of nodes, MUST be a common colour for the whole graph
                   opacity = 0.9,              # opacity of nodes. 0=transparent. 1=no transparency
                   zoom = T                    # Can you zoom on the figure?
)

p

library(igraph)
library(networkD3)

data2 <- data_frame(
  from=c("A", "A", "B", "C", "D", "E"),
  to=c("B", "F", "C", "D", "E", "F")
  
)

p2 <- simpleNetwork(data2, height="100px", width="100px",        
                    Source = 1,                 # column number of source
                    Target = 2,                 # column number of target
                    linkDistance = 10,          # distance between node. Increase this value to have more space between nodes
                    charge = -900,                # numeric value indicating either the strength of the node repulsion (negative value) or attraction (positive value)
                    fontSize = 14,               # size of the node names
                    fontFamily = "serif",       # font og node names
                    linkColour = "#666",        # colour of edges, MUST be a common colour for the whole graph
                    nodeColour = "#69b3a2",     # colour of nodes, MUST be a common colour for the whole graph
                    opacity = 0.9,              # opacity of nodes. 0=transparent. 1=no transparency
                    zoom = T                    # Can you zoom on the figure?
)

p2


require(htmlwidgets)
saveWidget(p2, file="path/widget.html")


