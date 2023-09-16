 # 【vue3, composionAPI】リアクティブな変数を定義する
 ## ref() もしくは reactive() を使用する
 ### ref() を使用する場合
 #### 特徴
 - template 内で参照する場合は.value をつけなくて良い
 - プリミティブ型、オブジェクトのどちらに対しても使用できる
 <br>

 ### reactive() を使用する場合
 #### 特徴
 - 別のオブジェクトにラップされず、オブジェクト自体がリアクティブになる。そのため、常に .value が不要
 - プリミティブ型には使用できない
   - 以下の例だと、コンソールにエラーメッセージが出力される他、値の変更が検知されない
```
<script setup>
import { reactive } from 'vue'

const reactive_primitive = reactive(1) //value cannot be made reactive: 1
const reactive_object = reactive(["a", "b"]) // ok

console.log(reactive_primitive)
console.log(reactive_object)

</script>

<template>
  <div>
    <button @click="reactive_primitive++">reactive_primitive</button>
    <p>reactive_primitive : {{ reactive_primitive }}</p> <!-- クリックで値を変更しても反映されない -->
    <button @click="reactive_object.push('push!')">reactive_object</button>
  </div>
</template>
 ```

 ### どちらを使用するべき？
 reactive() では以下のような制約があることから、公式ドキュメントでは基本的に ref() の使用が推奨されている
 - reactive() ではプリミティブ型を保持できない
 - オブジェクト全体を置換できない
 - 分割代入できない

 参考 https://ja.vuejs.org/guide/essentials/reactivity-fundamentals.html#limitations-of-reactive

 ## 算出プロパティ
 ### 変数を用いてリアクティブな状態を宣言する場合
 ref(), reactive() に変数を渡した場合、戻り値は元の変数のプロキシとなるため、元の変数の変更は検知されない <br>
 元の変数の変更を検知したい場合は、computed() によって定義した算出プロパティを使用する
 - 以下の例では、ボタンを押す毎に x がインクリメントされるが、computed で定義した値だけが再計算される

```vue.js
<script setup>
import { ref, computed } from 'vue'
const x = ref(1)
const calculate_with_ref = ref(x.value)
const calculate_with_computed = computed(() => x.value + 1) // 算出プロパティの定義
</script>

<template>
  <div>
    <button @click="x++">x is {{ x }}</button>
    <p>ref : {{ calculate_with_ref }}</p>
    <p>computed : {{ calculate_with_computed }}</p>
  </div>
</template>
```

