## zh-CN

通过 `content` 设置 字符串数组 指定多行文字水印内容。

## en-US

Use `content` to set a string array to specify multi-line text watermark content.
```tsx
import React from 'react';
import { Watermark } from 'antd';

const App: React.FC = () => (
  <Watermark content={['Ant Design', 'Happy Working']}>
    <div style={{ height: 500 }} />
  </Watermark>
);

export default App;
```
