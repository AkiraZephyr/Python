library(dplyr)

cat("=== Head of mtcars ===\n")
print(head(mtcars))

# Splitting the dataset
library(caTools)

split <- sample.split(mtcars$vs, SplitRatio = 0.8)

train_reg <- subset(mtcars, split == TRUE)
test_reg <- subset(mtcars, split == FALSE)

# Building the model
cat("\n=== Logistic Regression Model ===\n")
logistic_model <- glm(vs ~ wt + disp, data = train_reg, family = binomial)
print(logistic_model)

cat("\n=== Model Summary ===\n")
print(summary(logistic_model))

# Predicting test data based on model
cat("\n=== Predicted Probabilities ===\n")
predict_reg <- predict(logistic_model, test_reg, type = "response")
print(predict_reg)

# Convert probabilities to binary class labels (threshold = 0.5)
cat("\n=== Predicted Classes ===\n")
predicted_class <- ifelse(predict_reg > 0.5, 1, 0)
print(predicted_class)

# Plotting a Confusion Matrix
library(ggplot2)
library(reshape2)
conf_matrix <- table(test_reg$vs, predicted_class)
# Reshape the confusion matrix for ggplot2
conf_matrix_melted <- as.data.frame(conf_matrix)
colnames(conf_matrix_melted) <- c("Actual", "Predicted", "Count")

cat("\n=== Confusion Matrix ===\n")
print(conf_matrix)

cat("\n=== Confusion Matrix Heatmap ===\n")
print(
    ggplot(conf_matrix_melted, aes(x = Actual, y = Predicted, fill = Count)) +
        geom_tile() +
        geom_text(aes(label = Count), color = "black", size = 6) +
        scale_fill_gradient(low = "white", high = "blue") +
        labs(
            title = "Confusion Matrix Heatmap",
            x = "Actual",
            y = "Predicted"
        ) +
        theme_minimal()
)
