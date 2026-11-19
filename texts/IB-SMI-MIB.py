#
# PySNMP MIB module IB-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/infoblox/IB-SMI-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:36:27 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, Gauge32, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, enterprises, Bits, Integer32, iso, ModuleIdentity, ObjectIdentity, Opaque, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Gauge32", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "enterprises", "Bits", "Integer32", "iso", "ModuleIdentity", "ObjectIdentity", "Opaque", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
infoblox = ModuleIdentity((1, 3, 6, 1, 4, 1, 7779))
infoblox.setRevisions(('2017-01-24 00:00', '2015-05-19 00:00', '2013-10-03 00:00', '2013-08-12 00:00', '2012-03-27 00:00', '2008-01-14 00:00', '2005-01-10 00:00', '2004-05-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: infoblox.setRevisionsDescriptions(('Added oid for IB-FLEX and copyright update', 'Added definitions for Opaque Float', 'Added definitions for OM-license models, updated street-address and copyright update', 'Added new products and copyright update', 'Updated REVISION for new product update and copyright update', 'Updated copyright and CONTACT_INFO', 'Added copyright', 'Creation of the MIB file',))
if mibBuilder.loadTexts: infoblox.setLastUpdated('201701240000Z')
if mibBuilder.loadTexts: infoblox.setOrganization('Infoblox')
if mibBuilder.loadTexts: infoblox.setContactInfo('Infoblox\n                        3111 Coronado Drive\n                        Santa Clara, CA 95054\n                        1-888-463-6259\n\t                support@infoblox.com')
if mibBuilder.loadTexts: infoblox.setDescription('This is the MIB module for object type definitions\n\t    that are used throughout the infoblox enterprise MIBs.')
infobloxProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1))
ibDefault = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1000))
ibRsp2 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1001))
ibCisco = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1002))
ibVm = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1003))
ibVnios = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1004))
ib1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1101))
ib1200 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1102))
ib500 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1103))
ib550 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1201))
ib1050 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1202))
ib1550 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1203))
ib1552 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1204))
ib2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1205))
ib250 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1206))
ib1220 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1207))
ib550a = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1301))
ib1050a = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1302))
ib1550a = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1303))
ib1552a = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1304))
ib1852a = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1305))
ib250a = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1306))
ib2000a = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1307))
ib810 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1401))
ib820 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1402))
ib1410 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1403))
ib1420 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1404))
ib1400 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1405))
ib800 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1406))
pt1400 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1407))
ib2200 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1411))
ib2210 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1412))
ib2220 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1413))
pt2200 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1414))
ib4010 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1421))
ib4030 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1422))
ib4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1423))
pt4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1424))
ib4020 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1425))
ib100 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1431))
nd800 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1441))
nd1400 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1442))
nd2200 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1443))
nd4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1444))
ib815 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1501))
ib825 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1502))
ib1415 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1503))
ib1425 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1504))
ib1405 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1505))
ib805 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1506))
pt1405 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1507))
ib2205 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1511))
ib2215 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1512))
ib2225 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1513))
pt2205 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1514))
ib4015 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1521))
ib4035 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1522))
ib4005 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1523))
pt4005 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1524))
ib4025 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1525))
nd805 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1541))
nd1405 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1542))
nd2205 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1543))
nd4005 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1544))
ibflex = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1551))
ib906 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1601))
ib1506 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1602))
ib1606 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1603))
ib2306 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1604))
ib4106 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1605))
ib_926 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1606)).setLabel("ib-926")
nd_906 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1607)).setLabel("nd-906")
ib_1516 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1608)).setLabel("ib-1516")
ib_1526 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1609)).setLabel("ib-1526")
nd_1606 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1610)).setLabel("nd-1606")
ib_2326 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1611)).setLabel("ib-2326")
nd_2306 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1612)).setLabel("nd-2306")
ib_4126 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1613)).setLabel("ib-4126")
nd_4106 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1614)).setLabel("nd-4106")
tr_5005 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1615)).setLabel("tr-5005")
ibSNMP = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3))
ibProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1))
ibOne = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1))
ibTrapOne = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1))
ibPlatformOne = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2))
ibDNSOne = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3))
ibDHCPOne = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4))
ibDataplaneOne = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 5))
ibDNSServ = MibIdentifier((1, 3, 6, 1, 4, 1, 32))
ibDHCPServ = MibIdentifier((1, 3, 6, 1, 4, 1, 9999))
class IbString(TextualConvention, OctetString):
    description = 'A text string with 300 octets'
    status = 'current'
    displayHint = '300a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 300)

class IbNode(TextualConvention, OctetString):
    description = 'A node name string'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class IbIpAddr(TextualConvention, OctetString):
    description = 'An Ip address in xxx.xxx.xxx.xxx notation'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class IbIpv6Addr(TextualConvention, OctetString):
    description = 'An Ipv6 address in semicolon notation'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 46)

class IbFloat(TextualConvention, Opaque):
    description = 'A float value'
    status = 'current'
    subtypeSpec = Opaque.subtypeSpec + ValueSizeConstraint(7, 7)
    fixedLength = 7

mibBuilder.exportSymbols("IB-SMI-MIB", pt4000=pt4000, nd1400=nd1400, ibDNSServ=ibDNSServ, ib1200=ib1200, nd_1606=nd_1606, ibVm=ibVm, nd805=nd805, infobloxProducts=infobloxProducts, ibPlatformOne=ibPlatformOne, ib2220=ib2220, ib_1526=ib_1526, ib2225=ib2225, ib1506=ib1506, pt4005=pt4005, ib4000=ib4000, ib1400=ib1400, ibProduct=ibProduct, ib1050=ib1050, ib1405=ib1405, tr_5005=tr_5005, nd4000=nd4000, ib1000=ib1000, ib2000a=ib2000a, nd4005=nd4005, ib4106=ib4106, ib1552=ib1552, nd2200=nd2200, PYSNMP_MODULE_ID=infoblox, ib1550a=ib1550a, ibTrapOne=ibTrapOne, ib2215=ib2215, ib1420=ib1420, ibDataplaneOne=ibDataplaneOne, ib4010=ib4010, ib1852a=ib1852a, pt2205=pt2205, ib820=ib820, ibDHCPServ=ibDHCPServ, IbNode=IbNode, pt2200=pt2200, ib1425=ib1425, ibOne=ibOne, ib1550=ib1550, nd1405=nd1405, ib_2326=ib_2326, ib805=ib805, ibRsp2=ibRsp2, ibSNMP=ibSNMP, IbIpAddr=IbIpAddr, ibDNSOne=ibDNSOne, nd_906=nd_906, pt1405=pt1405, nd2205=nd2205, ib550a=ib550a, ib100=ib100, ib_926=ib_926, nd_2306=nd_2306, ib2306=ib2306, ib1552a=ib1552a, ib4025=ib4025, ib1050a=ib1050a, ib4005=ib4005, ib4015=ib4015, ibDefault=ibDefault, ib1410=ib1410, ib1415=ib1415, ib810=ib810, nd_4106=nd_4106, ibflex=ibflex, ib4030=ib4030, ib1220=ib1220, infoblox=infoblox, ibDHCPOne=ibDHCPOne, ib1606=ib1606, IbFloat=IbFloat, ib500=ib500, ibCisco=ibCisco, ib550=ib550, ib_4126=ib_4126, ib825=ib825, nd800=nd800, pt1400=pt1400, ibVnios=ibVnios, IbString=IbString, ib250=ib250, ib906=ib906, ib250a=ib250a, ib2205=ib2205, ib800=ib800, ib2210=ib2210, ib2000=ib2000, ib4020=ib4020, IbIpv6Addr=IbIpv6Addr, ib_1516=ib_1516, ib4035=ib4035, ib815=ib815, ib2200=ib2200)
