## zh-CN

省市联动是典型的例子，联动场景我们更推荐使用 [Cascader](/components/cascader-cn/) 组件。

## en-US

Coordinating the selection of provinces and cities is a common use case and demonstrates how selection can be coordinated. [Cascader](/components/cascader) component is strongly recommended in this case.
```tsx
import React, { useState } from 'react';
import { Select, Space } from 'antd';

const provinceData = ['Zhejiang', 'Jiangsu'];

const cityData = {
  Zhejiang: ['Hangzhou', 'Ningbo', 'Wenzhou'],
  Jiangsu: ['Nanjing', 'Suzhou', 'Zhenjiang'],
};

type CityName = keyof typeof cityData;

const App: React.FC = () => {
  const [cities, setCities] = useState(cityData[provinceData[0] as CityName]);
  const [secondCity, setSecondCity] = useState(cityData[provinceData[0] as CityName][0]);

  const handleProvinceChange = (value: CityName) => {
    setCities(cityData[value]);
    setSecondCity(cityData[value][0]);
  };

  const onSecondCityChange = (value: CityName) => {
    setSecondCity(value);
  };

  return (
    <Space wrap>
      <Select
        defaultValue={provinceData[0]}
        style={{ width: 120 }}
        onChange={handleProvinceChange}
        options={provinceData.map((province) => ({ label: province, value: province }))}
      />
      <Select
        style={{ width: 120 }}
        value={secondCity}
        onChange={onSecondCityChange}
        options={cities.map((city) => ({ label: city, value: city }))}
      />
    </Space>
  );
};

export default App;
```
