# Vue3 においてページ初期化時に、axios で取得したデータが反映されない
## 問題のコード
 - ブログサイトを作成していた際に、自作の api から記事の情報を取得・表示するため、以下のコードを作成した。
 - ArticleComponent に取得したデータを渡して表示するというもの
 - しかし、画面には何も表示されない

```
<script setup>
import ArticleComponent from '../components/ArticleComponent.vue';
import axios from 'axios';

articles = []

await axios.get('http://127.0.0.1/api/articles')
  .then(response => (articles = response.data))
  .catch(error => {
    console.log(error);
  });
</script>

<template>
  <div id="body">
    <ul id="articles">
      <ArticleComponent v-for="article in articles" :key="article.title" :title="article.title" :body="article.body" class="article"/>
    </ul>
  </div>
</template>
```

## 原因
 - コンポーネントがマウントされた後にコールバック関数を用いて、articles の値を更新しないと取得したデータが反映されない

## 対策
### おけるマウントとは
 - vue インスタンスを実際のHTML要素に関連付けること
 - 例えば、main.js では以下のように使用される
 
 ```
 createApp(App).use(router).mount('#app')
 ```

### データを反映させる方法
#### onMounted() を使用する
 - コンポーネントがマウントされた後に呼び出される関数
 - 参考 https://ja.vuejs.org/api/composition-api-lifecycle.html#onmounted

#### 修正後のコード
```
<script setup>
import ArticleComponent from '../components/ArticleComponent.vue';
import axios from 'axios';
import { onMounted, ref } from 'vue';

const articles = ref(null);
onMounted(async () => {
  try {
    const response = await axios.get('http://127.0.0.1/api/articles')
    if (response.status === 200) {
      articles.value = response.data;
    }
    else {
      console.error('Failed to fetch data:', response.status, response.statusText);
    }
  }
  catch (error) {
    console.log(error);
  }});
</script>

<template>
  <div id="body">
    <ul id="articles">
      <ArticleComponent v-for="article in articles" :key="article.title" :title="article.title" :body="article.body" class="article"/>
    </ul>
  </div>
</template>
```