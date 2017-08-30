---
title: "Weekly notes text analysis"
output: html_notebook
---

```{r}
library(readr)
library(tibble)
library('dplyr')
```

```{r}
weeknotes_ryan <- as_tibble(read_csv('projectes/nlp_test/weeknotes_ryan.csv', col_names = FALSE))
names(weeknotes_ryan) <- c( "s02e01",
                            "s01e09",
                            "s01e08",
                            "s01e07",
                            "s01e06",
                            "s01e05",
                            "s01e04",
                            "s01e03",
                            "s01e02",      
                            "s01e01"
       )
```



```{r}
weeknotes_ryan$cases <- 1
```

```{r}
weeknotes_ryan %>% 
  gather(cases, "episode", "text", 1:10) -> tidy_notes
```

