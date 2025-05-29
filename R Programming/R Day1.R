name <- "Satya"
print(paste("Welcome to R,",name))
print(name)

a <- 10
b = 20
c = a+b
d <- c*2
e = b^2
f = sqrt(100)
g <- log(1000)
print(paste("Value of A is",a))
print(paste("Value of B is",b))
print(paste("Value of C is",c))
print(paste("Value of D is",d))
print(paste("Value of E is",e))
print(paste("Value of F is",f))
print(paste("Value of G is",g))

#Data Types

age <- 20
Cname <- "Satya"
is_passed <- TRUE
# Type checks
class(age)
class(Cname)
class(is_passed)
typeof(age)
is.logical(is_passed)

# Vectors
scores <- c(90, 85, 88)
names <- c("Alice", "Bob", "Charlie")
mix <- c(10, "R", TRUE)  # coercion to character

# Vector operations
scores + 5              # adds 5 to each score
length(scores)          # number of elements
