## zh-CN

测试自定义 lineWidth 的情况：https://github.com/ant-design/ant-design/issues/46307

## en-US

测试自定义 lineWidth 的情况：https://github.com/ant-design/ant-design/issues/46307
```tsx
import React from 'react';
import { Checkbox, ConfigProvider } from 'antd';

const App: React.FC = () => (
  <>
    <ConfigProvider
      theme={{
        components: {
          Checkbox: {
            lineWidth: 6,
          },
        },
      }}
    >
      <Checkbox checked />
      <Checkbox />
    </ConfigProvider>
    <Checkbox checked />
    <Checkbox />
  </>
);

export default App;
```
