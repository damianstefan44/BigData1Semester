object l7z4 {
  import scala.math._
  import scala.util.Random._


  def p(x: Int): Int = Integer.numberOfLeadingZeros(x) + 1


  def mean() = {

    val n = pow(2,20).toInt
    val stoch = stochasticCountingAlgorithm(n)
    var sum = 0
    var i = 0
    while (i < stoch.length) {
      sum += pow(2,stoch(i)).toInt
      i += 1
    }
    println(sum)
    harmonic_mean(stoch)
  }

  def harmonic_mean(stoch: Array[Int]) = {

    val n = pow(2,20).toInt
    var sum = 0.0
    var i = 0
    while (i < stoch.length) {
      sum += (1.0/pow(2,stoch(i))).toDouble
      i += 1
    }
    println((256*256/sum).toInt*0.7182)
  }

  def exact() = {

    val n = pow(2,20).toInt

    val numbers = for ( _ <- 1 to n) yield nextInt()
    println(numbers.distinct.length)

  }


  def stochasticCountingAlgorithm(n: Int) = {

    val len = 256
    val M = Array.fill(256){0}

    for ( _ <- 1 to n){

      val random = nextInt()
      val px = p(random)
      val number = Math.floorMod(random,len)

      if(px > M(number)) M(number) = px
    }
    M
  }


  def main(args:Array[String]):Unit = {

   // val n3 = pow(2,28).toInt
   // val stoch3 = stochasticCountingAlgorithm(n3)

    mean()
    exact()
    // mean 8316928
    // harmonic 1290046
    // exact 1048460


  }

}
