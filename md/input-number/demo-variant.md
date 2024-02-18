## zh-CN

形态变体。

## en-US

Variants of InputNumber.
```tsx
import React from 'react';
import { Flex, InputNumber } from 'antd';

const App: React.FC = () => (
  <Flex vertical gap={12}>
    <InputNumber placeholder="Outlined" style={{ width: 200 }} />
    <InputNumber placeholder="Filled" variant="filled" style={{ width: 200 }} />
    <InputNumber placeholder="Borderless" variant="borderless" style={{ width: 200 }} />
  </Flex>
);

export default App;
```
