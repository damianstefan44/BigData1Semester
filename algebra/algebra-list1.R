make_matrix_from_vectors <- function(vector_list){
  len <- length(vector_list)
  return(matrix(unlist(vector_list), ncol = len))
}

make_matrix_from_vectors(list(c(2,2,2),c(3,4,5)))

normalize_vector <- function(vector) {
  return (vector/sqrt(sum(vector^2)))
}

normalize_matrix <- function(matrix) {
  for(column in 1:ncol(matrix)){
    matrix[,column] = normalize_vector(matrix[,column])
  }
  return(matrix)
}

check_orthagonality_vectors <- function(vector_list){
  M <- make_matrix_from_vectors(vector_list)
  MT <- t(M)
  outcome <- M %*% MT
  outcome_normalized <- normalize_matrix(outcome)
  diagonal <- diag(length(vector_list))
  decision1 <- setequal(outcome,diagonal)
  decision2 <- setequal(outcome_normalized,diagonal)
  if(decision1 | decision2){
    return(TRUE)
  }
  return(FALSE)
}

check_orthagonality_matrix <- function(matrix){
  M <- matrix
  MT <- t(M)
  outcome <- M %*% MT
  outcome_normalized <- normalize_matrix(outcome)
  diagonal <- diag(ncol(M))
  decision1 <- setequal(outcome,diagonal)
  decision2 <- setequal(outcome_normalized,diagonal)
  if(decision1 | decision2){
    return(TRUE)
  }
  return(FALSE)
}


check_orthagonality_vectors(list(c(0,0,2,0),c(0,0,0,2),c(0,2,0,0),c(2,0,0,0)))

check_orthagonality_vectors(list(c(0,0,1,0),c(0,0,0,1),c(0,1,0,0),c(1,0,0,0)))

library(geometry)

proj <- function(u, v) {
  return(dot(u, v)/dot(u,u)*u)
}


gramSchmidt = function(matrix) {
  
  res = matrix(0, nrow(matrix), ncol(matrix))
  
  for (col in 1:ncol(matrix)) {
    res[,col] = matrix[,col]
    
    if (col > 1) {
      for (i in 1:(col - 1)) {
        res[,col] = res[,col] - proj(res[,i], matrix[,col])
      }
    }
  }
  return(normalize_matrix(res))
}


m = matrix(c(5, 2, 6, 1), 2, 2)

gramSchmidt(m)

gramSchmidt2 = function(matrix) {
  matrix %*% solve(chol(t(matrix) %*% matrix))
}

gramSchmidt2(m)


getRandomMatrix = function(int) {
  i <- int
  repeat {
    randMatrix = matrix(c(sample(1:9999999, i*i, replace=TRUE)), ncol=i, nrow=i)
    if (det(randMatrix) != 0) {
      return(randMatrix)
    }
  }
}

randomMatrix = getRandomMatrix(1)
print(randomMatrix)

performance = function(int) {
  n <- int
  
  perf_v1 = c(1:n + 1)*0
  perf_v2 = c(1:n + 1)*0
  
  for(i in 1:n){
    
    m = getRandomMatrix(i)
    
    start1 = Sys.time()
    gramSchmidt(m)
    stop1 = Sys.time()
    perf_v1[i] = stop1 - start1
    
    start2 = Sys.time()
    gramSchmidt2(m)
    stop2 = Sys.time()
    perf_v2[i] = stop2 - start2
  }
  
  plot(1:n, perf_v1,
       main = "Speed comparison",
       xlab = "size",
       ylab = "time",
       type = "l",
       col = "blue",
       )
  lines(1:n, perf_v2, col="red")
  legend("topleft",
         c("with loops","without loops"),
         fill=c("blue","red")
  )
}
performance(100)
