object UseRationals {
  import Element.elem
  import Rational._
  import scala.language.implicitConversions
  implicit def intToRational(x: Int) = new Rational(x)


  def main(args:Array[String]):Unit = {

    val lhs = elem(frac(4, 0)) + elem(frac(2, 14))
    val rhs = elem(frac(4, 0) + frac(2, 14))
    println(lhs equals rhs)


  }
}

