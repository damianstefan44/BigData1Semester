import Element.elem
object RationalNumber {

  def rational(nom: Int, denom: Int = 1): Element = {
    val rational = elem(nom,denom)
    rational

  }
  def main(args: Array[String]) = {

    if(args.length == 1){
      val arg1 = args(0).toInt
      println(rational(arg1))
    }
    else if(args.length == 2){
      val arg1 = args(0).toInt
      val arg2 = args(1).toInt
      println(rational(arg1, arg2))
    }

  }
}
