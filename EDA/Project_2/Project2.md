Exploratory Data Analysis:Project 1
======================================
Created by Krish Mahajan 

### Basic settings

```r
echo = TRUE  # Always make code visible
options(scipen = 1)  # Turn off scientific notations for numbers
```


```r
# Loads RDS
NEI <- readRDS("data/summarySCC_PM25.rds")

SCC <- readRDS("data/Source_Classification_Code.rds")

# Samples data for testing
NEIsample <- NEI[sample(nrow(NEI), size = 1000, replace = F), ]

# Aggregates
Emissions <- aggregate(NEI[, 'Emissions'], by = list(NEI$year), FUN = sum)
Emissions$PM <- round(Emissions[, 2] / 1000, 2)

png(filename = "plot1.png")
barplot(Emissions$PM, names.arg = Emissions$Group.1, main = expression('Total Emission of PM'[2.5]), xlab = 'Year', ylab = expression(paste('PM', ''[2.5], ' in Kilotons')))
dev.off()
```

```
## RStudioGD 
##         2
```


```r
NEI_Baltimore<-NEI[NEI$fips=="24510", c("Emissions","year","fips")]
Emissions <- aggregate(NEI_Baltimore[, 'Emissions'], by = list(NEI_Baltimore$year), FUN = sum)
Emissions$PM <- round(Emissions[, 2] / 1000, 2)

png(filename = "plot2.png")
barplot(Emissions$PM, names.arg = Emissions$Group.1, main = expression('Total Emission of PM [2.5] in Baltimore' ), xlab = 'Year', ylab = expression(paste('PM', ''[2.5], ' in Kilotons')))
dev.off()
```

```
## RStudioGD 
##         2
```


```r
MD <- subset(NEI, fips == 24510)
MD$year <- factor(MD$year, levels = c('1999', '2002', '2005', '2008'))
png('plot3.png', width = 800, height = 500, units = 'px')
qplot(x=year,y=log(Emissions),data=MD,geom="boxplot",facets=.~type,xlab='Year',ylab=('Log of PM[2.5] Emissions'),main='Emissions per Type in Baltimore City, Maryland',alpha=0.8,fill='gear')
```

```
## Warning: Removed 19 rows containing non-finite values (stat_boxplot).
```

```
## Warning: Removed 18 rows containing non-finite values (stat_boxplot).
```

```
## Warning: Removed 91 rows containing non-finite values (stat_boxplot).
```

```r
#ggplot(data = MD, aes(x = year, y = log(Emissions))) + facet_grid(. ~ type) + guides(fill = F) + geom_boxplot(aes(fill = type)) + stat_boxplot(geom = 'errorbar') + ylab(expression(paste('Log', ' of PM'[2.5], ' Emissions'))) + xlab('Year') + ggtitle('Emissions per Type in Baltimore City, Maryland') + geom_jitter(alpha = 0.10)

dev.off()
```

```
## RStudioGD 
##         2
```


```r
# Coal-related SCC
SCC.coal = SCC[grepl("coal", SCC$Short.Name, ignore.case = TRUE), ]

# Merges two data sets
merge <- merge(x = NEI, y = SCC.coal, by = 'SCC')
merge.sum <- aggregate(merge[, 'Emissions'], by = list(merge$year), sum)
colnames(merge.sum) <- c('Year', 'Emissions')

png(filename = 'plot4.png')
qplot(x=Year,y=log(Emissions),data=merge.sum,xlab='Year',geom='line',ylab=('Log of PM[2.5] Emissions'),main='Emissions through coal in united states',alpha=0.8,fill='gear')
#ggplot(data = merge.sum, aes(x = Year, y = Emissions / 1000)) + geom_line(aes(group = 1, col = Emissions)) + geom_point(aes(size = 2, col = Emissions)) + ggtitle(expression('Total Emissions of PM'[2.5])) + ylab(expression(paste('PM', ''[2.5], ' in kilotons'))) + geom_text(aes(label = round(Emissions / 1000, digits = 2), size = 2, hjust = 1.5, vjust = 1.5)) + theme(legend.position = 'none') + scale_colour_gradient(low = 'black', high = 'red')
dev.off()
```

```
## RStudioGD 
##         2
```


```r
# Baltimore City, Maryland == fips
MD.onroad <- subset(NEI, fips == 24510 & type == 'ON-ROAD')

# Aggregates
MD.df <- aggregate(MD.onroad[, 'Emissions'], by = list(MD.onroad$year), sum)
colnames(MD.df) <- c('year', 'Emissions')

png('plot5.png')
ggplot(data = MD.df, aes(x = year, y = Emissions)) + geom_bar(aes(fill = year), stat = "identity") + guides(fill = F) + ggtitle('Total Emissions of Motor Vehicle Sources in Baltimore City, Maryland') + ylab(expression('PM'[2.5])) + xlab('Year') + theme(legend.position = 'none') + geom_text(aes(label = round(Emissions, 0), size = 1, hjust = 0.5, vjust = 2))
dev.off()
```

```
## RStudioGD 
##         2
```

```r
# Baltimore City, Maryland
# Los Angeles County, California
MD.onroad <- subset(NEI, fips == '24510' & type == 'ON-ROAD')
CA.onroad <- subset(NEI, fips == '06037' & type == 'ON-ROAD')

# Aggregates
MD.DF <- aggregate(MD.onroad[, 'Emissions'], by = list(MD.onroad$year), sum)
colnames(MD.DF) <- c('year', 'Emissions')
MD.DF$City <- paste(rep('MD', 4))

CA.DF <- aggregate(CA.onroad[, 'Emissions'], by = list(CA.onroad$year), sum)
colnames(CA.DF) <- c('year', 'Emissions')
CA.DF$City <- paste(rep('CA', 4))

DF <- as.data.frame(rbind(MD.DF, CA.DF))

png('plot6.png')
ggplot(data = DF, aes(x = year, y = Emissions)) + geom_bar(aes(fill = year),stat = "identity") + guides(fill = F) + ggtitle('Total Emissions of Motor Vehicle Sources\nLos Angeles County, California vs. Baltimore City, Maryland') + ylab(expression('PM'[2.5])) + xlab('Year') + theme(legend.position = 'none') + facet_grid(. ~ City) + geom_text(aes(label = round(Emissions, 0), size = 1, hjust = 0.5, vjust = -1))
dev.off()
```

```
## RStudioGD 
##         2
```
