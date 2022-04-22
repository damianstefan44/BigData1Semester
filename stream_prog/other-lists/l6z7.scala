object l6z7 {


  def main(args:Array[String]):Unit = {

    val f = (i:Int) => Option(i * i)
    val g = (i:Int) => Option(i * i * i)
    val m = Some(2)

    val x = 5

    //LAWS for m = Some(2)
    println(((m flatMap f) flatMap g) == (m flatMap (x => f(x) flatMap g)))
    println((Some(x) flatMap f) == f(x))
    println((m flatMap (x => Some(x))) == m)

    val m2 = None

    //LAWS for m = None
    println(((m2 flatMap f) flatMap g) == (m2 flatMap (x => f(x) flatMap g)))
    println((Some(x) flatMap f) == f(x))
    println((m2 flatMap (x => Some(x))) == m2)
    
  }

}
