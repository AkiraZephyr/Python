#1.	Simple Regression

# Dataset 1: Student Scores vs Hours Studied
hours <- c(1, 2, 3, 4, 5, 6, 7, 8, 9)
scores <- c(35, 40, 50, 55, 60, 65, 70, 80, 85)

data1 <- data.frame(hours, scores)

# Model
model1 <- lm(scores ~ hours, data = data1)
summary(model1)

# Predict
pred1 <- predict(model1, newdata = data1)

# Plot
plot(data1$hours, data1$scores, col="blue", pch=16,
     xlab="Hours Studied", ylab="Scores", main="Simple Linear Regression")
abline(model1, col="red", lwd=2)

#2.	Multiple Linear Regression
sqft <- c(1000, 1200, 1500, 1800, 2000, 2200, 2500)
bedrooms <- c(2, 3, 3, 4, 4, 5, 5)
price <- c(200000, 250000, 270000, 320000, 360000, 400000, 450000)

data <- data.frame(sqft, bedrooms, price)
print(data)
model <- lm(price ~ sqft + bedrooms, data = data)
summary(model)
predictions <- predict(model, newdata = data)
print(predictions)
data$predicted_price <- predictions
print(data)
install.packages("scatterplot3d")
library(scatterplot3d)

# 3D scatter plot
s3d <- scatterplot3d(data$sqft, data$bedrooms, data$price, 
                     pch = 16, color = "blue", 
                     xlab = "Square Feet", ylab = "Bedrooms", zlab = "Price", 
                     main = "Multiple Linear Regression")

# Add regression plane
s3d$plane3d(model, draw_polygon = TRUE, draw_lines = TRUE, color = "red")





#3.	Ridge Regression

install.packages("glmnet")   # For ridge regression
install.packages("ggplot2")  # For plotting
library(glmnet)
library(ggplot2)
sqft <- c(1000, 1200, 1500, 1800, 2000, 2200, 2500)
bedrooms <- c(2, 3, 3, 4, 4, 5, 5)
price <- c(200000, 250000, 270000, 320000, 360000, 400000, 450000)

data <- data.frame(sqft, bedrooms, price)
print(data)
X <- as.matrix(data[, c("sqft", "bedrooms")])

# Response variable
y <- data$price
ridge_model <- glmnet(X, y, alpha = 0)

# View model details
print(ridge_model)
plot(ridge_model, xvar = "lambda", label = TRUE)
title("Ridge Regression Coefficients vs Lambda")

set.seed(123)
cv_ridge <- cv.glmnet(X, y, alpha = 0)

# Best lambda
best_lambda <- cv_ridge$lambda.min
print(best_lambda)

# Plot CV error
plot(cv_ridge)
title("Cross-Validation for Lambda Selection")


ridge_pred <- predict(cv_ridge, s = best_lambda, newx = X)

# Add predictions to dataset
data$predicted_price <- ridge_pred
print(data)

ggplot(data, aes(x = price, y = predicted_price)) +
  geom_point(color = "blue", size = 3) +
  geom_abline(intercept = 0, slope = 1, color = "red", linetype = "dashed") +
  labs(title = "Ridge Regression: Actual vs Predicted Prices",
       x = "Actual Price", y = "Predicted Price") +
  theme_minimal()