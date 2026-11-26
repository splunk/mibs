#
# PySNMP MIB module CISCO-DNS-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DNS-CLIENT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDNSClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 888))
ciscoDNSClientCapability.setRevisions(('2004-11-25 00:00', '2004-08-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDNSClientCapability.setRevisionsDescriptions(("Added the agent capabilities \n                 'cDNSClientCapSanOSV20R1MDS9000' for\n                 SanOS 2.0(1) on Cisco MDS 9000 series devices.", 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDNSClientCapability.setLastUpdated('200411250000Z')
if mibBuilder.loadTexts: ciscoDNSClientCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDNSClientCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoDNSClientCapability.setDescription('The capabilities description of\n                CISCO-DNS-CLIENT-MIB.')
cDNSClientCapSanOSV20R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 888, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDNSClientCapSanOSV20R1MDS9000 = cDNSClientCapSanOSV20R1MDS9000.setProductRelease('Cisco SanOS 2.0(1) on Cisco MDS 9000\n                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDNSClientCapSanOSV20R1MDS9000 = cDNSClientCapSanOSV20R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: cDNSClientCapSanOSV20R1MDS9000.setDescription('Cisco DNS Client MIB capabilities')
mibBuilder.exportSymbols("CISCO-DNS-CLIENT-CAPABILITY", ciscoDNSClientCapability=ciscoDNSClientCapability, PYSNMP_MODULE_ID=ciscoDNSClientCapability, cDNSClientCapSanOSV20R1MDS9000=cDNSClientCapSanOSV20R1MDS9000)
