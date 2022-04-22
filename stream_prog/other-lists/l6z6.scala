object l6z6 {
  import scala.math._
  import scala.util.Random._


  def p(x: Int): Int = Integer.numberOfLeadingZeros(x) + 1

  def stochasticCountingAlgorithm(n: Int) = {
    var M = 0
    for ( _ <- 1 to n){

      val random = nextInt()
      val px = p(random)

      if(px > M) M = px
    }
    M
  }


  
  def main(args:Array[String]):Unit = {

    val n1 = pow(2,20).toInt
    val stoch1 = pow(2,stochasticCountingAlgorithm(n1)).toInt

    println(s"n = $n1 , 2^m = $stoch1")

    val n2 = pow(2,24).toInt
    val stoch2 = pow(2,stochasticCountingAlgorithm(n2)).toInt

    println(s"n = $n2 , 2^m = $stoch2")

    val n3 = pow(2,28).toInt
    val stoch3 = pow(2,stochasticCountingAlgorithm(n3)).toInt

    println(s"n = $n3 , 2^m = $stoch3")
  }

}
