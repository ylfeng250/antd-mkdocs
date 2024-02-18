## zh-CN

可以通过 `status` 的值控制二维码的状态，提供了 `active`、`expired`、`loading`、`scanned` 四个值。

## en-US

The status can be controlled by the value `status`, four values ​​of `active`, `expired`, `loading`, `scanned` are provided.
```tsx
import React from 'react';
import { Flex, QRCode } from 'antd';

const value = 'https://ant.design';

const App: React.FC = () => (
  <Flex gap="middle" wrap="wrap">
    <QRCode value={value} status="loading" />
    <QRCode value={value} status="expired" onRefresh={() => console.log('refresh')} />
    <QRCode value={value} status="scanned" />
  </Flex>
);

export default App;
```
