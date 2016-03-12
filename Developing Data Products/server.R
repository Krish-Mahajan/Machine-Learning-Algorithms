library(shiny)
library(RCurl)
library(caret)
mpg <- getURL("http://robertkevinackerman.com/wp-content/uploads/2014/08/mpg.csv")
mpg <- read.csv(text = mpg)
modFit <- train(mpg ~ cyl + disp + horse + weight + accel + year + origin, method="glm", data=mpg)
shinyServer(
  function(input, output) { 
    #pred = predict(modFit, data)
    #output$prediction <- renderPrint ({as.string(pred)})
    output$prediction <- renderPrint ({
      cyl = input$cyl
      disp = input$disp
      horse = input$horse
      weight = input$weight
      accel = input$accel
      year = input$year
      origin = input$origin
      predict(modFit,data.frame(cyl, disp, horse, weight, accel, year, origin))})
  }
)