# CRUD_simple

Изготовить приложение, которое выполняет следующие функции:

* Вести справочник покупателей с полями: 
  * ФИО, 
  * год рождения, 
  * пол, 
  * дата регистрации в системе, 
  * согласие на обработку ПД, 
  * фото покупателя. 
  
  Реализовать CRUD flow для справочника
* Вести справочник наименование товаров которыми торгует магазин с полями: 
  * Наименование товара, 
  * стоимость закупки товара, 
  * стоимость продажи товара.  
  
  Реализовать CRUD flow для справочника.
* Вести реестр покупок с полями: 
  * ФИО покупателя (ссылка на покупателя), 
  * дата покупки. 

  Экземпляр строки реестра должен позволять вести в табличную часть: 
  * наименование покупаемого товара (ссылка на справочник наименований товаров), 
  * кол-во покупаемых единиц, 
  * стоимость единицы товара, 
  * суммарная стоимость товара (кол-во*стоимость продажи). 
  
  Реализовать CRUD flow для реестра и табличной части экземпляра строки реестра.
* Реализовать отчет который выводит всех покупателей и суммарную стоимость совершенных покупок. Параметры отчета: дата совершения покупок. Сортировка отчета должна осуществляться по убыванию суммарной стоимости покупок