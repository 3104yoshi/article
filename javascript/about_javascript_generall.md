JavaScript
 - DOMContentLoaded (in case loading js in the same html)
 - defer, async (in case loading outer js)

- difference between defer and async
 - defer : load js in the order of declaring
 - async : load js in parallel
 - If there is a dependency among js files, you should use defer.

- prototype
 - all javascript objects has prototype property
 - It is searched for property of prototype in case that the property can't be found in the object itself.
 - This search is cascaded until property is gotten or it reached to the end of chain. 

- shadowing property
 - 子クラスのプロパティが優先される

- assign
 - オブジェクトにプロトタイプを追加することができる