#
# PySNMP MIB module CISCO-IPSEC-SIGNALING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IPSEC-SIGNALING-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIPsecSigCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 488))
ciscoIPsecSigCapability.setRevisions(('2006-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIPsecSigCapability.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoIPsecSigCapability.setLastUpdated('200602020000Z')
if mibBuilder.loadTexts: ciscoIPsecSigCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIPsecSigCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoIPsecSigCapability.setDescription('Agent capabilities for\n                 CISCO-IPSEC-SIGNALING-MIB')
cIPsecSigCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 488, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIPsecSigCapSanOSV30R1MDS9000 = cIPsecSigCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIPsecSigCapSanOSV30R1MDS9000 = cIPsecSigCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: cIPsecSigCapSanOSV30R1MDS9000.setDescription('Cisco Generic IPsec/FC-SP Signaling\n                     MIB capabilities')
mibBuilder.exportSymbols("CISCO-IPSEC-SIGNALING-CAPABILITY", cIPsecSigCapSanOSV30R1MDS9000=cIPsecSigCapSanOSV30R1MDS9000, PYSNMP_MODULE_ID=ciscoIPsecSigCapability, ciscoIPsecSigCapability=ciscoIPsecSigCapability)
