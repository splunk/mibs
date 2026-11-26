#
# PySNMP MIB module CISCO-VIDEO-SESSION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VIDEO-SESSION-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
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
ciscoVideoSessionCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 599))
ciscoVideoSessionCapability.setRevisions(('2011-05-24 00:00', '2010-11-11 00:00',))
if mibBuilder.loadTexts: ciscoVideoSessionCapability.setLastUpdated('201105240000Z')
if mibBuilder.loadTexts: ciscoVideoSessionCapability.setOrganization('Cisco Systems, Inc.')
ciscoVideoSessionCapabilityV15R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 599, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV15R01 = ciscoVideoSessionCapabilityV15R01.setProductRelease('OS=IOS\n                     OSVERSION=15.1\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV15R01 = ciscoVideoSessionCapabilityV15R01.setStatus('current')
ciscoVideoSessionCapabilityV152T02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 599, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV152T02 = ciscoVideoSessionCapabilityV152T02.setProductRelease('OS=IOS\n                     OSVERSION=15.2(2)T\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV152T02 = ciscoVideoSessionCapabilityV152T02.setStatus('current')
mibBuilder.exportSymbols("CISCO-VIDEO-SESSION-CAPABILITY", ciscoVideoSessionCapabilityV15R01=ciscoVideoSessionCapabilityV15R01, ciscoVideoSessionCapabilityV152T02=ciscoVideoSessionCapabilityV152T02, ciscoVideoSessionCapability=ciscoVideoSessionCapability, PYSNMP_MODULE_ID=ciscoVideoSessionCapability)
