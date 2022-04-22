getMatrix = function(vectors) {
  return(matrix(unlist(vectors), ncol=length(vectors)))
}

getMatrix(list(c(1, 0, 0), c(0, 1, 0)))

scalar <- function(x) { x/sqrt(sum(x^2)) }

areOrthogonal <- function(v1, v2) { dot(v1, v2, d = TRUE) == 0 }

areAllOrthogonal = function(matrix) {
  for (col1 in 1:(sqrt(sum(xncol(matrix) - 1)))) {
    for (col2 in (col1 + 1):ncol(matrix)) {
      if (areOrthogonal(matrix[,col1], matrix[,col2]) == FALSE) {
        return(FALSE)
      }
    }
  }
  
  return(TRUE)
}

areAllOrthonormal = function(matrix) {
  for (col in 1:ncol(matrix)) {
    if (norm(as.matrix(matrix[,col])) != 1) {
      return(FALSE)
    }
  }
  
  return(areAllOrthogonal(matrix))
}

matrix = matrix(c(1,1,1,1,1,1,1,1,1),3,3)

areAllOrthonormal(matrix)



matrix = matrix(c(3, 1, 2, 2), 2, 2)
matrix = matrix(c(1, -1, 1, 1, 0, 1, 1, 1, 2), 3, 3)

projection <- function(u, v) { dot(u, v) / dot(u, u) * u }

normalize = function(matrix) {
  for (col in 1:ncol(matrix)) {
    matrix[,col] = scalar(matrix[,col])
  }
  return(matrix)
}

gramSchmidtWithLoops = function(matrix) {
  result = matrix(0, nrow(matrix), ncol(matrix))
  
  for (col in 1:ncol(matrix)) {
    result[,col] = matrix[,col]
    
    if (col > 1) {
      for (i in 1:(col - 1)) {
        result[,col] = result[,col] - projection(result[,i], matrix[,col])
      }
    }
  }
  
  return(normalize(result))
}

gramSchmidtVerifier = function(matrix) {
  if (areAllOrthogonal(matrix)) {
    result = normalize(matrix)
  } else {
    result = gramSchmidtWithLoops(matrix)
  }
  
  for (col in 1:ncol(result)) {
    if (!all.equal(sqrt(sum(result[,col]^2)), 1)) {
      print(sqrt(sum(result[,col]^2)))
      return(FALSE)
    }
  }
  
  return(result)
}

matrix = matrix(c(3, 1, 2, 2), 2, 2)
gramSchmidtVerifier(matrix)


# A^(-1) *path/tofile/here A = L * U
# Q = A * t(L^(-1))
# get chol(A^(-1) * A), it returns the upper triangular factor L
# then pass L to solve(L), gets t(L^(-1))
# And multply by A, A * t(L^(-1))
gramSchmidtWithoutLoops = function(matrix) {
  matrix %*% solve(chol(t(matrix) %*% matrix))
}

gramSchmidtWithoutLoops(matrix)
