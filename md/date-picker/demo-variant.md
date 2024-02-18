## zh-CN

可选 `outlined` `filled` `borderless` 三种形态。

## en-US

There are `outlined` `fille` and `borderless`, totally three variants to choose from.
```tsx
import React from 'react';
import { DatePicker, Flex } from 'antd';

const { RangePicker } = DatePicker;

const App: React.FC = () => (
  <Flex vertical gap={12}>
    <Flex gap={8}>
      <DatePicker placeholder="Outlined" />
      <RangePicker placeholder={['Outlined', '']} />
    </Flex>
    <Flex gap={8}>
      <DatePicker placeholder="Filled" variant="filled" />
      <RangePicker placeholder={['Filled', '']} variant="filled" />
    </Flex>
    <Flex gap={8}>
      <DatePicker placeholder="Borderless" variant="borderless" />
      <RangePicker placeholder={['Borderless', '']} variant="borderless" />
    </Flex>
  </Flex>
);

export default App;
```
