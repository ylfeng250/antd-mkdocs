## zh-CN

展示所有配置选项。

## en-US

Show all configured prop.
```tsx
import React from 'react';
import { Pagination } from 'antd';

const App: React.FC = () => (
  <Pagination
    total={85}
    showSizeChanger
    showQuickJumper
    showTotal={(total) => `Total ${total} items`}
  />
);

export default App;
```
