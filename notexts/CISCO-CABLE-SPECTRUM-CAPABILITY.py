#
# PySNMP MIB module CISCO-CABLE-SPECTRUM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CABLE-SPECTRUM-CAPABILITY
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
ciscoCableSpectrumCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoCableSpectrumCapability.setRevisions(('2002-12-18 00:00',))
if mibBuilder.loadTexts: ciscoCableSpectrumCapability.setLastUpdated('200212180000Z')
if mibBuilder.loadTexts: ciscoCableSpectrumCapability.setOrganization('Cisco Systems, Inc.')
ciscoCableSpectrumCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableSpectrumCapabilityV12R00 = ciscoCableSpectrumCapabilityV12R00.setProductRelease('Cisco IOS 12.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableSpectrumCapabilityV12R00 = ciscoCableSpectrumCapabilityV12R00.setStatus('current')
ciscoCableSpectrumCapabilityV12R01Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableSpectrumCapabilityV12R01Rev1 = ciscoCableSpectrumCapabilityV12R01Rev1.setProductRelease('Cisco IOS 12.1(05)EC and 12.2 BC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableSpectrumCapabilityV12R01Rev1 = ciscoCableSpectrumCapabilityV12R01Rev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-CABLE-SPECTRUM-CAPABILITY", ciscoCableSpectrumCapabilityV12R00=ciscoCableSpectrumCapabilityV12R00, ciscoCableSpectrumCapability=ciscoCableSpectrumCapability, PYSNMP_MODULE_ID=ciscoCableSpectrumCapability, ciscoCableSpectrumCapabilityV12R01Rev1=ciscoCableSpectrumCapabilityV12R01Rev1)
