#
# PySNMP MIB module CISCO-ITP-XUA-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ITP-XUA-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoItpXuaCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 268))
ciscoItpXuaCapability.setRevisions(('2008-06-25 00:00', '2007-09-26 00:00', '2006-10-05 00:00', '2004-11-03 00:00', '2003-10-15 00:00', '2003-08-15 00:00', '2002-05-08 00:00',))
if mibBuilder.loadTexts: ciscoItpXuaCapability.setLastUpdated('200806250000Z')
if mibBuilder.loadTexts: ciscoItpXuaCapability.setOrganization('Cisco Systems, Inc.')
ciscoItpXuaCapabilityV12R0204MB5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0204MB5 = ciscoItpXuaCapabilityV12R0204MB5.setProductRelease('Cisco IOS 12.2(4)MB5')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0204MB5 = ciscoItpXuaCapabilityV12R0204MB5.setStatus('current')
ciscoItpXuaCapabilityV12R0219SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0219SW = ciscoItpXuaCapabilityV12R0219SW.setProductRelease('Cisco IOS 12.2(19)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0219SW = ciscoItpXuaCapabilityV12R0219SW.setStatus('current')
ciscoItpXuaCapabilityV12R0223SW01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0223SW01 = ciscoItpXuaCapabilityV12R0223SW01.setProductRelease('Cisco IOS 12.2(23)SW01')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0223SW01 = ciscoItpXuaCapabilityV12R0223SW01.setStatus('current')
ciscoItpXuaCapabilityV12R0225SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0225SW = ciscoItpXuaCapabilityV12R0225SW.setProductRelease('Cisco IOS 12.2(25)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0225SW = ciscoItpXuaCapabilityV12R0225SW.setStatus('current')
ciscoItpXuaCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0218IXA = ciscoItpXuaCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0218IXA = ciscoItpXuaCapabilityV12R0218IXA.setStatus('current')
ciscoItpXuaCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0411SW = ciscoItpXuaCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0411SW = ciscoItpXuaCapabilityV12R0411SW.setStatus('current')
ciscoItpXuaCapabilityV12R0415SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0415SW = ciscoItpXuaCapabilityV12R0415SW.setProductRelease('Cisco IOS 12.4(15)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0415SW = ciscoItpXuaCapabilityV12R0415SW.setStatus('current')
ciscoItpXuaCapabilityV12R0218IXE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0218IXE = ciscoItpXuaCapabilityV12R0218IXE.setProductRelease('Cisco IOS 12.2(18)IXE')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0218IXE = ciscoItpXuaCapabilityV12R0218IXE.setStatus('current')
ciscoItpXuaCapabilityV12R0233IRA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0233IRA = ciscoItpXuaCapabilityV12R0233IRA.setProductRelease('Cisco IOS 12.2(33)IRA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0233IRA = ciscoItpXuaCapabilityV12R0233IRA.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-XUA-CAPABILITY", ciscoItpXuaCapabilityV12R0233IRA=ciscoItpXuaCapabilityV12R0233IRA, ciscoItpXuaCapabilityV12R0225SW=ciscoItpXuaCapabilityV12R0225SW, ciscoItpXuaCapabilityV12R0218IXA=ciscoItpXuaCapabilityV12R0218IXA, ciscoItpXuaCapabilityV12R0218IXE=ciscoItpXuaCapabilityV12R0218IXE, ciscoItpXuaCapabilityV12R0219SW=ciscoItpXuaCapabilityV12R0219SW, PYSNMP_MODULE_ID=ciscoItpXuaCapability, ciscoItpXuaCapabilityV12R0223SW01=ciscoItpXuaCapabilityV12R0223SW01, ciscoItpXuaCapability=ciscoItpXuaCapability, ciscoItpXuaCapabilityV12R0411SW=ciscoItpXuaCapabilityV12R0411SW, ciscoItpXuaCapabilityV12R0204MB5=ciscoItpXuaCapabilityV12R0204MB5, ciscoItpXuaCapabilityV12R0415SW=ciscoItpXuaCapabilityV12R0415SW)
