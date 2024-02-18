## zh-CN

翻转后如果不够则偏移以供完全的展示。

## en-US

Shift the popup if not enough space after flip.
```tsx
import React from 'react';
import { Select } from 'antd';

const App: React.FC = () => (
  <Select
    style={{ width: 120, marginTop: '50vh' }}
    open
    options={new Array(100).fill(null).map((_, index) => ({
      value: index,
    }))}
  />
);

export default App;
```
