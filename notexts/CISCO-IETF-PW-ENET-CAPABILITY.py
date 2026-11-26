#
# PySNMP MIB module CISCO-IETF-PW-ENET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IETF-PW-ENET-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
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
ciscoIetfPwEnetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 428))
ciscoIetfPwEnetCapability.setRevisions(('2004-11-29 12:00',))
if mibBuilder.loadTexts: ciscoIetfPwEnetCapability.setLastUpdated('200411291200Z')
if mibBuilder.loadTexts: ciscoIetfPwEnetCapability.setOrganization('Cisco Systems, Inc.')
ciscoIetfPwEnetCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 428, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfPwEnetCapabilityV12R00 = ciscoIetfPwEnetCapabilityV12R00.setProductRelease('Cisco IOS 12.0(28)S, Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfPwEnetCapabilityV12R00 = ciscoIetfPwEnetCapabilityV12R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-PW-ENET-CAPABILITY", ciscoIetfPwEnetCapability=ciscoIetfPwEnetCapability, ciscoIetfPwEnetCapabilityV12R00=ciscoIetfPwEnetCapabilityV12R00, PYSNMP_MODULE_ID=ciscoIetfPwEnetCapability)
