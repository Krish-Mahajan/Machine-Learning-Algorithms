library(shiny)
library(caret)
shinyUI (
  pageWithSidebar (
    # Application title
    headerPanel ("Predict Your Vehicle's MPG"),
    
    sidebarPanel (
      numericInput('cyl', 'Cylinders', 4, min = 3, max= 8, step = 1),
      numericInput('disp', 'Displacement', 190, min = 70, max= 450, step = 10),
      numericInput('horse', 'Horsepower', 100, min = 50, max= 230, step = 5),
      numericInput('weight', 'Weight', 3000, min = 1650, max= 5000, step = 50),
      numericInput('accel', 'Acceleration', 15, min = 8, max= 24, step = 1),
      numericInput('year', 'Year', 75, min = 70, max= 82, step = 1),
      numericInput('origin', 'Origin', 2, min = 1, max= 3, step = 1),
      submitButton('Submit')
      ),
    mainPanel (
      h3 ('Results of prediction'),
      h4 ('Your Vehicle\'s Predicted MPG:'),
      textOutput("prediction")
      )
    )

)