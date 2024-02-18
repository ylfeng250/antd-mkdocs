## zh-CN

在某些场景下，需要定制计数能力（例如 emoji 长度以 1 计算），可以通过 `count` 属性来实现。在该模式下，通过 `count.max` 属性来超出原生 `maxLength` 的限制。

## en-US

It is necessary to customize the counting ability in some scenarios (such as emoji length is counted as 1), which can be achieved through the `count` attribute. Use `count.max` attribute exceeds the limit of the native `maxLength`.
```tsx
import React from 'react';
import { Flex, Input, Typography } from 'antd';
import { runes } from 'runes2';

const App: React.FC = () => (
  <Flex vertical gap={16}>
    <div>
      <Typography.Title level={5}>Exceed Max</Typography.Title>
      <Input
        count={{
          show: true,
          max: 10,
        }}
        defaultValue="Hello, antd!"
      />
    </div>

    <div>
      <Typography.Title level={5}>Emoji count as length 1</Typography.Title>
      <Input
        count={{
          show: true,
          strategy: (txt) => runes(txt).length,
        }}
        defaultValue="🔥🔥🔥"
      />
    </div>

    <div>
      <Typography.Title level={5}>Not exceed max</Typography.Title>
      <Input
        count={{
          show: true,
          max: 6,
          strategy: (txt) => runes(txt).length,
          exceedFormatter: (txt, { max }) => runes(txt).slice(0, max).join(''),
        }}
        defaultValue="🔥 antd"
      />
    </div>
  </Flex>
);

export default App;
```
