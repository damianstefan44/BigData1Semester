object TailRecFactorial {
import scala.annotation.tailrec
def tailFactorial(n: BigInt): BigInt = {
  @tailrec
  def go(acc: 	BigInt, n: BigInt): BigInt = {
    if (n <= 1) acc
    else go(n * acc, n - 1)
  }
  go(1, n)
}

//@tailrec

def factorial(n: BigInt): BigInt = {
    if (n <= 1) 1
    else n * factorial(n-1)
}
def main(args:Array[String]):Unit = {
  try{
    val n = args(0).toInt
    println(factorial(n))
    //println(tailFactorial(n))
  }
  catch{
    case e: NumberFormatException => println("Wrong input!")    
  }
}
}
