# Vue3 においてページ初期化時に、axios で取得したデータを表示したい
## 概要
 - ブログサイトを作成しており、自作の api から記事の情報を取得・表示したい
 - 少しハマったのでメモ


## 方法
### データを反映させる方法
#### onMounted() を使用する
 - コンポーネントがマウントされた後に呼び出される関数
 - マウントとは：vue インスタンスを実際のHTML要素に関連付けること
 - 参考 https://ja.vuejs.org/api/composition-api-lifecycle.html#onmounted

#### サンプルコード
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

 - ArticleComponent に取得したデータを渡して表示している